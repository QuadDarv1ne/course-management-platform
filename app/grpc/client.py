import grpc
import course_pb2
import course_pb2_grpc

def get_course_details(course_id: str):
    channel = grpc.insecure_channel('localhost:50051')
    stub = course_pb2_grpc.CourseServiceStub(channel)
    response = stub.GetCourseDetails(course_pb2.CourseRequest(course_id=course_id))
    print("Course Title:", response.title)
    print("Course Description:", response.description)

if __name__ == "__main__":
    get_course_details("1")
