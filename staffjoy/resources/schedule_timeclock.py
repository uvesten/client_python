from ..resource import Resource


class ScheduleTimeclock(Resource):
    """this is only a get collection endpoint"""
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}/schedules/{schedule_id}/timeclocks/"
