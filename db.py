from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb+srv://admin:admin@cluster.xaq58zj.mongodb.net/?appName=Cluster")

db = client["student_db1"]

student_collection = db["students"]

course_collection = db["courses"]