ten = input('Nhập vào Họ và Tên: ')
toan = input('Nhập vào Điểm Môn Toán: ')
van = input('Nhập vào Điểm Môn Văn: ')
anh = input('Nhập vào Điểm Môn Anh: ')

diemToan = float(toan)
diemVan = float(van)
diemAnh = float(anh)

DTB = round(((diemToan + diemVan + diemAnh) / 3), 2)
print('Học sinh ', ten, " đạt điểm TB các môn là: ", DTB)
