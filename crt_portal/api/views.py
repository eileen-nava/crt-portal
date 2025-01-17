from cts_forms.models import Report, ResponseTemplate
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from cts_forms.views import mark_report_as_viewed
from rest_framework.permissions import IsAuthenticated
from api.serializers import ReportSerializer, ResponseTemplateSerializer
from django.contrib.auth.decorators import login_required

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}


@api_view(['GET'])
@login_required
def api_root(request, format=None):
    return Response({
        'reports': reverse('api:report-list', request=request, format=format),
        'responses': reverse('api:response-list', request=request, format=format)
    })


class ReportList(generics.ListAPIView):
    """
    API endpoint that allows Reports to be viewed.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Report.objects.all().order_by('pk')
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportDetail(generics.RetrieveUpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        report_pk = kwargs.get("pk")
        if report_pk:
            report = Report.objects.filter(pk=report_pk).first()
            if not report.viewed:
                mark_report_as_viewed(report, request.user)
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        report_pk = kwargs.get("pk")
        if report_pk:
            report = Report.objects.filter(pk=report_pk).first()
            if not report.viewed:
                mark_report_as_viewed(report, request.user)
        return self.update(request, *args, **kwargs)


class ResponseList(generics.ListAPIView):
    """
    API endpoint that allows responses to be viewed.
    """
    queryset = ResponseTemplate.objects.all()
    serializer_class = ResponseTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResponseDetail(generics.RetrieveAPIView):
    queryset = ResponseTemplate.objects.all()
    serializer_class = ResponseTemplateSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        template = self.get_object()
        serializer = self.get_serializer(template)
        # Makes a copy of the serialized data so it can be updated
        serialized_data = serializer.data
        # If a `?report_id=<pk>` is provided, then render the letter content
        # with the given report details
        report_pk = request.query_params.get('report_id')
        if report_pk:
            report = Report.objects.filter(pk=report_pk).first()
            serialized_data['url'] = serialized_data['url'] + '?report_id=' + report_pk
            serialized_data['subject'] = template.render_subject(report)
            serialized_data['body'] = template.render_body(report)
        return Response(serialized_data)
