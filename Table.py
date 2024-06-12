# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dormitory.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# class DormManager(db.Model):
#     __tablename__ = 'DormManager'
#     DormManagerID = db.Column(db.String(10), primary_key=True, unique=True, comment='宿管编号')
#     DormManagerName = db.Column(db.String(5), comment='宿管姓名')
#     DormManagerAccount = db.Column(db.String(15), comment='管理员账号')
#     DormManagerPasswd = db.Column(db.String(15), comment='管理员密码')
#     BuildingNo = db.Column(db.String(10), comment='楼宇号')
#
#
# class StuDorm(db.Model):
#     __tablename__ = 'StuDorm'
#     DormNo = db.Column(db.String(10), primary_key=True, unique=True, comment='寝室号')
#     RoomNo = db.Column(db.String(5), comment='房间号')
#     LivePeoNo = db.Column(db.SmallInteger, comment='当前入住人数')
#     BuildingNo = db.Column(db.String(10), comment='楼宇号')
#     FloorNo = db.Column(db.String(10), comment='楼层号')
#
#
# class Stu(db.Model):
#     __tablename__ = 'Stu'
#     Sno = db.Column(db.String(10), primary_key=True, unique=True, comment='学生学号')
#     SAccount = db.Column(db.String(15), comment='学生账号')
#     SPasswd = db.Column(db.String(15), comment='学生密码')
#     SName = db.Column(db.String(5), comment='学生姓名')
#     SDormNo = db.Column(db.String(10), db.ForeignKey('StuDorm.DormNo', onupdate="CASCADE", ondelete="CASCADE"),
#                         comment='学生寝室号')
#     BedNo = db.Column(db.SmallInteger, comment='床号')
#     LiveState = db.Column(db.String(3), comment='入住状态')
#
#
# class ManageStu(db.Model):
#     __tablename__ = 'ManageStu'
#     ManagerID = db.Column(db.String(10),
#                           db.ForeignKey('DormManager.DormManagerID', onupdate="CASCADE", ondelete="CASCADE"),
#                           comment='宿管编号')
#     Sno = db.Column(db.String(10), db.ForeignKey('Stu.Sno', onupdate="CASCADE", ondelete="CASCADE"), comment='学生学号')
#     SetPasswd = db.Column(db.String(15), comment='设置学生密码')
#     __table_args__ = (db.PrimaryKeyConstraint('ManagerID', 'Sno'),)
#
#
# class DormInfo(db.Model):
#     __tablename__ = 'DormInfo'
#     InfoID = db.Column(db.String(20), primary_key=True, unique=True, comment='通知编号')
#     InfoContent = db.Column(db.String(50), comment='具体通知')
#     InfoTime = db.Column(db.Date, comment='通知时间')
#     InfoLocation = db.Column(db.String(10), comment='通知地点')
#     DormManagerID = db.Column(db.String(10),
#                               db.ForeignKey('DormManager.DormManagerID', onupdate="CASCADE", ondelete="CASCADE"),
#                               comment='宿管编号')
#     CheckNo = db.Column(db.SmallInteger, comment='已查看学生数')
#
#
# class CheckInfo(db.Model):
#     __tablename__ = 'CheckInfo'
#     CheckState = db.Column(db.String(3), comment='查看状态')
#     Sno = db.Column(db.String(10), db.ForeignKey('Stu.Sno', onupdate="CASCADE", ondelete="CASCADE"), comment='学生学号')
#     InfoID = db.Column(db.String(20), db.ForeignKey('DormInfo.InfoID', onupdate="CASCADE", ondelete="CASCADE"),
#                        comment='通知编号')
#     __table_args__ = (db.PrimaryKeyConstraint('Sno', 'InfoID'),)
#
#
# class GoodsAccess(db.Model):
#     __tablename__ = 'Goods_Access'
#     Goods_number = db.Column(db.String(5), primary_key=True, unique=True, comment='物品编号')
#     Goods_status = db.Column(db.String(3), comment='存取状态')
#     Goods_name = db.Column(db.String(10), comment='物品名称')
#     Goods_describe = db.Column(db.String(30), comment='物品描述')
#     Sno_takeout = db.Column(db.String(10), db.ForeignKey('Stu.Sno', onupdate="CASCADE", ondelete="CASCADE"),
#                             comment='取出学生学号')
#
#
# class WEManage(db.Model):
#     __tablename__ = 'WE_Manage'
#     BuildingNo = db.Column(db.String(10), comment='楼宇号')
#     SDormNo = db.Column(db.String(10), db.ForeignKey('StuDorm.DormNo', onupdate="CASCADE", ondelete="CASCADE"),
#                         primary_key=True, unique=True, comment='寝室号')
#     WE_Present = db.Column(db.Numeric, comment='当前水电费')
#     WE_History = db.Column(db.Numeric, comment='历史水电费')
#     Payment_status = db.Column(db.String(3), comment='缴费状态')
#
#
# class RepairRequest(db.Model):
#     __tablename__ = 'Repair_Request'
#     Repair_request_id = db.Column(db.String(10), primary_key=True, unique=True, comment='提交请求编号')
#     Repair_status = db.Column(db.String(10), comment='维修状态')
#     Repair_starttime = db.Column(db.Date, comment='维修提交时间')
#     Repair_endtime = db.Column(db.Date, comment='维修结束时间')
#     Sno = db.Column(db.String(10), db.ForeignKey('Stu.Sno', onupdate="CASCADE", ondelete="CASCADE"), comment='学生学号')
#
#
# class HealthEvaluation(db.Model):
#     __tablename__ = 'Health_evaluation'
#     SDormNo = db.Column(db.String(10), db.ForeignKey('StuDorm.DormNo', onupdate="CASCADE", ondelete="CASCADE"),
#                         primary_key=True, unique=True, comment='寝室号')
#     Score = db.Column(db.Numeric, comment='总分')
#     CountTime = db.Column(db.Date, comment='统计时间')
#     Ranking = db.Column(db.SmallInteger, comment='排名')
#
#
# class PersonAccess(db.Model):
#     __tablename__ = 'PersonAccess'
#     RegNo = db.Column(db.String(10), primary_key=True, comment='登记编号')
#     AccessName = db.Column(db.String(5), comment='姓名')
#     ContactInfo = db.Column(db.String(15), comment='联系方式')
#     AccessReason = db.Column(db.String(50), comment='访问原因')
#     EntryTime = db.Column(db.Date, comment='进入时间')
#     LeaveTime = db.Column(db.Date, comment='离开时间')
#
#
# @app.route('/')
# def fetch_all_data_from_stu():
#     try:
#         with app.app_context():
#             # rs = conn.execute(sqlalchemy.text("SELECT * FROM Stu"))
#             results = Stu.query.all()
#             # results = rs.fetchall()
#
#             if results:
#                 result_str = "<br>".join([f"{stu.id}, {stu.name}, {stu.age}" for stu in results])
#                 print(result_str)  # 输出到控制台
#                 return result_str  # 返回结果到浏览器
#             else:
#                 return "No data found in table Stu"
#     except Exception as e:
#         return str(e)  # 返回错误信息
#
#
# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)
