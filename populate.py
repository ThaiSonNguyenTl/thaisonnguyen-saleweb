from models.clothers import Clothers
from models.mancloth import Mancloth
from random import randint
import mlab
mlab.connect()

# list_cloth= [ { "title" : "Áo thun sọc ngang cổ rộng",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/188/1571046845.jpg"
#         },
#         { "title" : "Áo thun mắt tay dài",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/188/1570593828.jpg"
#         },
#         { "title" : "Áo thun đan No Problemo",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/188/1570593701.jpg"
#         },
#         { "title" : "Áo thun đan minh họa",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/188/1570593568.jpg"
#         },
#         { "title" : "Áo thun Brooklyn",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/188/1570593345.jpg"
#         },
#         { "title" : "Áo thun đan Mental mũ",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/189/1570593199.jpg"
#         },
#         { "title" : "Áo thun trễ vai đính sợi",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/188/1570593083.jpg"
#         },
#         { "title" : "Áo thun phối vàng",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/188/1570592933.jpg"
#         },
#         { "title" : "Áo thun dài Mathilda",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/265/1570592400.jpg"
#         },
#         { "title" : "Áo sơ mi jean",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/179/1569835275.jpg"
#         },
#         { "title" : "Áo khoác da cổ bẻ",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/178/1569765392.jpg"
#         },
#         { "title" : "Áo khoác da lộn",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/205/1569489918.jpg"
#         },
#         { "title" : "Áo jean 2 nửa 2 màu",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/179/1569152927.jpg"
#         },
#         { "title" : "Áo jean đan dây 2 bên eo",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/179/1569152451.jpg"
#         },
#         { "title" : "Áo sơ mi jean túi nắp",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/179/1567141009.jpg"
#         },
#         { "title" : "Áo jean nút ngọc trai",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/179/1565666366.jpg"
#         },
#         { "title" : "Quần training rộng",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/212/1570008157.jpg"
#         },
#          { "title" : "Quần gấu xếp ly",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/212/1570007962.jpg"
#         },
#          { "title" : "Quần lanh",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/212/1570007560.jpg"
#         },
#          { "title" : "Quần lưng thun",
#             "image" : "http://www.stylehanquoc.com/shopping/images/product/212/1569924672.jpg"
#         },
#           ]
# for i in list_cloth:
    # clother = Clothers( title = i["title"],
    #                     image = i["image"],
    #                     price = randint(10,50),
    #                     gender = randint(0,1)
    # )
    # clother.save()
# clother = Mancloth( title = "Áo khoác bò",
#                     image = "https://www.dhresource.com/0x0/f2/albu/g6/M01/84/F9/rBVaSFpwW_eAec8hAAiiIC7VsAo210.jpg",
#                     price = randint(100000,500000),
                 
#                     )
# clother.save()
# allclother = Mancloth.objects()
# print(allclother)
# allclother.delete()
# print(allclother)
list_man = [
    {
        "title" : "Áo Thun Trắng Phối Sọc",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/DSC05044-600x943.jpg"         
    },
    {
        "title" : "Áo Thun Đen Phối Sọc",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/3-1-600x943.jpg"         
    },
    {
        "title" : "Áo Thun Đen In Chữ",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/9-1-600x943.jpg"         
    },
    {
        "title" : "Áo Thun Trắng In Chữ",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/7-600x943.jpg"         
    },
    {
        "title" : "Áo Thun Sọc Nâu In DREAMCHASER",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8503-600x943.jpg"         
    },
    {
        "title" : "Áo Thun Trắng In Chữ",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/08/3-1-600x943.jpg"         
    },
    {
        "title" : "Áo Sơ Mi Kem Họa Tiết",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8795-600x943.jpg"         
    },
    {
        "title" : "Áo Sơ Mi Đen Phối Hoa",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8839-600x943.jpg"         
    },
    {
        "title" : "Áo Sơ Mi Xanh Sọc Trắng Vàng",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8428-600x943.jpg"         
    },
    {
        "title" : "Áo Sơ Mi Caro Cam Xanh",
        "image" : "https://www.celeb.vn/wp-content/uploads/2018/10/8S26-1-600x943.png"         
    },
    {
        "title" : "Áo Sơ Mi Caro Xanh Vàng",
        "image" : "https://www.celeb.vn/wp-content/uploads/2018/10/IMG_2023-600x943.jpg"         
    },
    {
        "title" : "Áo Khoác Dù Nón Xám Phối Trắng",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/06/8-600x943.jpg"         
    },
    {
        "title" : "Áo Khoác Dù Nón Đen Phối Xanh",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/07/7-2-600x943.jpg"         
    },
    {
        "title" : "Áo Khoác Dù Nón Xanh Phối Đen",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/07/6-2-600x943.jpg"         
    },
    {
        "title" : "Áo Khoác Dù Đen Phối 3 Sọc",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/07/áo-khoác-1-600x943.jpg"         
    },
    {
        "title" : "Quần Jean Xanh Trơn",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/DSC05809-600x943.jpg"         
    },
    {
        "title" : "Quần Jean Xám Wash",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/DSC05080-600x943.jpg"         
    },
    {
        "title" : "Quần Jean Xanh Xước",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8059-600x943.jpg"         
    },
    {
        "title" : "Quần Jean Xanh Rách In Chữ",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8556-600x943.jpg"         
    },
    {
        "title" : "Quần Jean Trắng Trơn",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8402-2.jpg"         
    },
    {
        "title" : "Quần Jean Xanh Nhạt",
        "image" : "https://www.celeb.vn/wp-content/uploads/2019/07/9Q09-3-1-600x943.jpg"         
    },
    {
        "title" : "Áo khoác bò",
        "image" : "https://www.dhresource.com/0x0/f2/albu/g6/M01/84/F9/rBVaSFpwW_eAec8hAAiiIC7VsAo210.jpg"         
    },
    {
        "title" : "Áo gió nam",
        "image" : "//product.hstatic.net/1000289385/product/mausac-be_23053be6_358a7db43b4e4843a51ac7c12f158537_large.jpg"         
    },
    {
        "title" : "ÁO khoác nam KAZUKI KIMONO ",
        "image" : "//product.hstatic.net/1000289385/product/mausac-xam_23049gr1_bd3e74b855bc41cc93c6b6784b4eb6bc_large.jpg"         
    },


]

for i in list_man:
    clother = Mancloth( title = i["title"],
                         image = i["image"],
                         price = randint(150000,500000),
                        
    )
    clother.save()

# cloth = Mancloth.objects()
# for i in cloth:    
#     print(i['id'])  // get all id from collection