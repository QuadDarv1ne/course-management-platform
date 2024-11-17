import grpc
from concurrent import futures
import time
import course_pb2
import course_pb2_grpc

class CourseService(course_pb2_grpc.CourseServiceServicer):
    def GetCourseDetails(self, request, context):
        return course_pb2.CourseDetails(title="Python Basics", description="Learn Python from scratch")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_pb2_grpc.add_CourseServiceServicer_to_server(CourseService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051")
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
