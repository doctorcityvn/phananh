from __future__ import unicode_literals
from django.db import models
from django import forms
from django.conf import settings
import django.utils.safestring as safestring
import datetime

class Division(models.Model):
    div=models.Manager()
    namediv = models.CharField('Phòng khám ', max_length=200)
    active = models.BooleanField("Is Active", default=True)

    def __str__(self):
        return self.namediv
class Patient(models.Model):
    City_s = (
        ('Hà Nội','Hà Nội'),
        ('Hà Nam','Hà Nam'),
        ('TP. Hồ Chí Minh','TP. Hồ Chí Minh'),
        ('Hải Phòng','Hải Phòng'),
        ('Thái Bình','Thái Bình'),
    )
    pat=models.Manager()
    Type_id = models.ForeignKey(Division, on_delete=models.CASCADE)
    codepatientp = models.CharField("Code bệnh nhân",default='BN1', max_length=10, primary_key=True)
    namepatient = models.CharField("Họ tên", max_length=200)
    age = models.IntegerField("Tuổi", default=40)
    place = models.CharField("Địa chỉ", max_length=200, null=True)
    City = models.CharField("Thành phố", max_length=200,choices=City_s,default='Hà Nội', null=True)
    ordering = ['codepatientp']
    def __str__(self):
        return self.namepatient
class Medicine(models.Model):
    M1 = (
        ('Kháng sinh','Kháng sinh'),
        ('Kháng viêm','Kháng viêm'),

    )
    M2 = (
        ('KS','Kháng sinh'),
        ('KV','Kháng viêm'),

    )
    medi=models.Manager()
    codemedicine = models.CharField("Code medicine",default='K', max_length=200, primary_key=True)
    name_medi = models.CharField("Tên thuốc", max_length=200)
    dosage = models.CharField("Liều dùng",default='', max_length=200)
    function1 = models.TextField("Công dụng", blank=True,null=True)
    sideeffect = models.TextField("Tác dụng phụ", blank=True,null=True)



    def __str__(self):
        return self.name_medi


class Typeservice(models.Model):
    S1 = (
        ('Chụp XQ','Chụp XQ'),
        ('Truyền máu','Truyền máu'),
        ('Điện não đồ','Điện não đồ'),
        ('Nội soi','Nội soi'),
        ('Siêu âm','Siêu âm'),
    )
    typeserv=models.Manager()
    codeservice = models.CharField("Code service",default='DV', max_length=200, primary_key=True)
    name_serv = models.CharField(max_length=200,choices=S1)
    def __str__(self):
        return self.name_serv

class Service(models.Model):
    serv=models.Manager()
    codeservice = models.ForeignKey(Typeservice, on_delete=models.CASCADE)
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField('Trạng thái', max_length=200,default='Đã gửi yêu cầu')
    lankham = models.CharField('Lần khám', max_length=3,default='1')
    date = models.DateField(("Ngày yêu cầu dịch vụ"), default=datetime.date.today)
    def __str__(self):
        return self.status
class Xlkhancap(models.Model):
    Xlkc_s = (
        ('Giảm đau bằng morphin','Giảm đau bằng morphin'),
        ('Trợ tim khẩn cấp','Trợ tim khẩn cấp'),
        ('Điện giải khẩn cấp','Điện giải khẩn cấp'),
        ('Truyền đạm','Truyền đạm'),
    )
    Xlkhancap1=models.Manager()
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name_xlkc = models.CharField('Tên xử lý khẩn cấp ', max_length=200)
    status = models.CharField('Trạng thái', max_length=200,default='Đã gửi yêu cầu')
    lankham = models.CharField('Lần khám',max_length=3,default='1')
    date = models.DateField(("Date"), default=datetime.date.today)
    def __str__(self):
        return self.name_xlkc
class Donthuoc(models.Model):
    Donthuoc1=models.Manager()
    codedonthuoc = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    soluong = models.CharField('Số lượng ', max_length=200,default='1')
    dvtinh = models.CharField('Đơn vị tính', max_length=200,default='vỉ')
    lankham = models.CharField('Lần khám', max_length=3,default='1')
    date = models.DateField(("Date"), default=datetime.date.today)
    def __str__(self):
        return self.soluong

class Ketluan(models.Model):
    ketluan1=models.Manager()
    codeketluan = models.CharField("Code kết luận",default='', max_length=200, primary_key=True)
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name_ketluan = models.TextField('Kết luận ', blank=True,null=True)
    bacsy = models.CharField('Bác sỹ', max_length=200)
    lankham = models.CharField('Lần khám', max_length=3,default='1')
    date = models.DateField(("Date"), default=datetime.date.today)
    def __str__(self):
        return self.name_ketluan

class Trieuchung(models.Model):
    Tctq_s = (
        ('Bất tỉnh','Bất tỉnh'),
        ('Mạch nhanh','Mạch nhanh'),
        ('Mạch chậm','Mạch chậm'),
        ('Tăng huyết áp tâm thu','Tăng huyết áp tâm thu'),
        ('tăng huyết áp tâm trường','tăng huyết áp tâm trường'),
        ('Mất máu','Mất máu'),
        ('Gẫy xương','Gẫy xương'),
        ('Giãn đồng tử','Giãn đồng tử'),
    )
    Nhomcq = (
        ('đầu','đầu'),
        ('tứ chi','tứ chi'),
        ('ngực','ngực'),
        ('hệ tuần hoàn','hệ tuần hoàn'),
        ('Hệ hô hấp','Hệ hô hấp'),
    )
    tchung=models.Manager()
    codetrieuchung = models.CharField("Code triệu chứng",default='', max_length=200, primary_key=True)
    trieuchung1 = models.CharField('Triệu chứng', max_length=200,choices=Tctq_s, default='Bất tỉnh')
    nhomcoquan = models.CharField('Nhóm cơ quan', max_length=200,choices=Nhomcq, default='Bất tỉnh')
    def get_first_image(self):
            return self.Trieuchungtq_set.all()
    def __str__(self):
        return self.trieuchung1

class Trieuchungtq(models.Model):
    trieuchungtqs=models.Manager()
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='codepatienttctq')
    codetrieuchung = models.ForeignKey(Trieuchung, on_delete=models.CASCADE, related_name='codetctqs')
    status1 = models.CharField('Trạng thái', max_length=2,default='1')
    lankham = models.CharField('Lần khám',max_length=3,default='1')
    date = models.DateField("Date", default=datetime.date.today)
    def __str__(self):
        return self.status1
class Trieuchungcb(models.Model):
    tccucbo=models.Manager()
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    codetrieuchung = models.ForeignKey(Trieuchung, on_delete=models.CASCADE)
    status1 = models.CharField('Trạng thái', max_length=2,default='1')
    lankham = models.CharField('Lần khám',max_length=3,default='1')
    date = models.DateField("Date", default=datetime.date.today)
    def __str__(self):
        return self.status1
class Bacsy(models.Model):
    bsy=models.Manager()
    codebs = models.CharField("Code:",default='', max_length=5, primary_key=True)
    hoten = models.CharField("Họ tên:",default='', max_length=200)
    diachi = models.CharField("Địa chỉ:",default='', max_length=200)
    thanhpho = models.CharField("Thành phố:",default='', max_length=200)
    mobile = models.CharField("Mobile",default='', max_length=200)
    email = models.CharField("Email:",default='', max_length=200)
    sochungchihanhnghe = models.CharField("Số Chứng chỉ hành nghề:",default='', max_length=200,blank=True,null=True)
    nghiepvu = models.CharField("Chuyên khoa",default='', max_length=200,blank=True,null=True)
    chucdanh = models.CharField("Chức danh",default='', max_length=200,blank=True,null=True)
    date = models.DateField(("Date ngày tham gia"), default=datetime.date.today)
    def __str__(self):
        return self.hoten
class Benhan(models.Model):
    ban=models.Manager()
    cba = models.CharField("Code:",default='', max_length=5, primary_key=True)
    bn = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bs = models.ForeignKey(Bacsy, on_delete=models.CASCADE)
    dnv = models.DateField(("Date ngày nhập viện"), default=datetime.date.today)
    dxv = models.DateField(("Date ngày xuất viện"), default=datetime.date.today)
    dttvp = models.DateField(("Date ngày thanh toán viện phí"), default=datetime.date.today)
class Trieuchungbenhnhan(models.Model):
    tcbn=models.Manager()
    cba = models.ForeignKey(Benhan, on_delete=models.CASCADE)
    ctt = models.ForeignKey(Trieuchung, on_delete=models.CASCADE)
    tt = models.CharField('Trạng thái', max_length=2,default='1')
    date = models.DateField("Date", default=datetime.date.today)
    def __str__(self):
        return self.status
class Xuly(models.Model):
    xl=models.Manager()
    cba = models.ForeignKey(Benhan, on_delete=models.CASCADE)
    txl = models.CharField('Tên xử lý khẩn cấp', max_length=200)
    tt = models.CharField('Trạng thái', max_length=2,default='1')
    date = models.DateField("Date", default=datetime.date.today)
    def __str__(self):
        return self.status
class Benhsu(models.Model):
    bs=models.Manager()
    cba = models.ForeignKey(Benhan, on_delete=models.CASCADE)
    tbx = models.TextField('Tên bệnh sử', max_length=200)
    date = models.DateField("Ngày nhập dữ liệu:", default=datetime.date.today)
    def __str__(self):
        return self.tbx

class Dichvuyeucau(models.Model):
    dv=models.Manager()
    cdv= models.CharField("Code:",default='', max_length=5, primary_key=True)
    cba = models.ForeignKey(Benhan, on_delete=models.CASCADE)
    tdv = models.CharField('Tên dịch vụ', max_length=200)
    tt = models.CharField('Trạng thái', max_length=2,default='1')
    date = models.DateField("Date", default=datetime.date.today)
    def __str__(self):
        return self.status1
class Donthuocdieutri(models.Model):
    dtdt=models.Manager()
    cdtdt = models.CharField("Code:",default='', max_length=5, primary_key=True)
    ct = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    cba = models.ForeignKey(Benhan, on_delete=models.CASCADE)
    sl = models.CharField('Số lượng ', max_length=200,default='1')
    dvt = models.CharField('Đơn vị tính', max_length=200,default='vỉ')
    date = models.DateField(("ngày kê đơn"), default=datetime.date.today)
    def __str__(self):
        return self.soluong
class Khachhang(models.Model):
    kh=models.Manager()
    ckh = models.CharField("Code:",default='', max_length=5, primary_key=True)
    ht= models.CharField("Họ tên:",default='', max_length=200)
    dc = models.CharField("Địa chỉ:",default='', max_length=200)
    tp = models.CharField("Thành phố:",default='', max_length=200)
    mb = models.CharField("Mobile",default='', max_length=200)
    em = models.CharField("Email:",default='', max_length=200)
    date = models.DateField(("Date ngày tham gia"), default=datetime.date.today)
    def __str__(self):
        return self.ht
class User1(models.Model):
    kh=models.Manager()
    ckh = models.CharField("Code:",default='', max_length=5, primary_key=True)
    ht= models.CharField("Họ tên:",default='', max_length=200)
    dc = models.CharField("Địa chỉ:",default='', max_length=200)
    tp = models.CharField("Thành phố:",default='', max_length=200)
    mb = models.CharField("Mobile",default='', max_length=200)
    em = models.CharField("Email:",default='', max_length=200)
    date = models.DateField(("Date ngày tham gia"), default=datetime.date.today)
    def __str__(self):
        return self.hoten
class Yeucau(models.Model):
    yc=models.Manager()
    cyc= models.CharField("Code:",default='', max_length=5, primary_key=True)
    cu = models.ForeignKey(Khachhang, on_delete=models.CASCADE)
    tdv = models.CharField('Tên dịch vụ', max_length=200)
    cl = models.CharField('Chất lượng', max_length=2,default='1')
    tt = models.BooleanField(default=True)
    bs = models.ForeignKey(Bacsy, on_delete=models.CASCADE)
    date = models.DateField("Ngày yêu cầu", default=datetime.date.today)
    def __str__(self):
        return self.status1


