from models.clothers import Clothers
from models.mancloth import Mancloth
from random import randint
import mlab
mlab.connect()

list_cloth= [ { "title" : "Áo thun sọc ngang cổ rộng",
            "image" : "../static/images/prodwoman1.jpg"
        },
        { "title" : "Áo thun mắt tay dài",
            "image" : "../static/images/prodwoman2.jpg"
        },
        { "title" : "Áo thun đan No Problemo",
            "image" : "../static/images/prodwoman3.jpg"
        },
        { "title" : "Áo thun đan minh họa",
            "image" : "../static/images/prodwoman4.jpg"
        },
        { "title" : "Áo thun Brooklyn",
            "image" : "../static/images/prodwoman5.jpg"
        },
        { "title" : "Áo thun đan Mental mũ",
            "image" : "../static/images/prodwoman6.jpg"
        },
        { "title" : "Áo thun trễ vai đính sợi",
            "image" : "../static/images/prodwoman7.jpg"
        },
        { "title" : "Áo thun phối vàng",
            "image" : "../static/images/prodwoman8.jpg"
        },
        { "title" : "Áo thun dài Mathilda",
            "image" : "../static/images/prodwoman9.jpg"
        },
        { "title" : "Áo sơ mi jean",
            "image" : "../static/images/prodwoman9.jpg"
        },
        { "title" : "Áo khoác da cổ bẻ",
            "image" :  "../static/images/prodwoman10.jpg"
        },
        { "title" : "Áo khoác da lộn",
            "image" :  "../static/images/prodwoman11.jpg"
        },
        { "title" : "Áo jean 2 nửa 2 màu",
            "image" :  "../static/images/prodwoman12.jpg"
        },
        { "title" : "Áo jean đan dây 2 bên eo",
            "image" :  "../static/images/prodwoman13.jpg"
        },
        { "title" : "Áo sơ mi jean túi nắp",
            "image" :  "../static/images/prodwoman14.jpg"
        },
        { "title" : "Áo jean nút ngọc trai",
            "image" :  "../static/images/prodwoman15.jpg"
        },
        { "title" : "Quần training rộng",
            "image" :  "../static/images/prodwoman16.jpg"
        },
         { "title" : "Quần gấu xếp ly",
            "image" :  "../static/images/prodwoman17.jpg"
        },
         { "title" : "Quần lanh",
            "image" : "../static/images/prodwoman18.jpg"
        },
         { "title" : "Quần lưng thun",
            "image" : "../static/images/prodwoman19.jpg"
        },
        { "title" : "Quần lưng thun",
            "image" : "../static/images/prodwoman20.jpg"
        },
        { "title" : "Quần lưng thun",
            "image" : "../static/images/prodwoman21.jpg"
        },
        { "title" : "Quần lưng thun",
            "image" : "../static/images/prodwoman22jpg"
        },
        { "title" : "Quần lưng thun",
            "image" : "../static/images/prodwoman23.jpg"
        },
        { "title" : "Quần lưng thun",
            "image" : "../static/images/prodwoman24.jpg"
        },
          ]
for i in list_cloth:
    clother = Clothers( title = i["title"],
                        image = i["image"],
                        price = randint(200000,1200000),
                       
    )
    clother.save()
# clother = Mancloth( title = "Áo khoác bò",
#                     image = "https://www.dhresource.com/0x0/f2/albu/g6/M01/84/F9/rBVaSFpwW_eAec8hAAiiIC7VsAo210.jpg",
#                     price = randint(100000,500000),
                 
#                     )
# clother.save()
# allclother = Clothers.objects()
# print(allclother)
# allclother.delete()
# print(allclother)
# list_man = [
#     {
#         "title" : "Áo Thun Trắng Phối Sọc",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/DSC05044-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Thun Đen Phối Sọc",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/3-1-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Thun Đen In Chữ",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/9-1-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Thun Trắng In Chữ",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/7-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Thun Sọc Nâu In DREAMCHASER",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8503-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Thun Trắng In Chữ",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/08/3-1-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Sơ Mi Kem Họa Tiết",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8795-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Sơ Mi Đen Phối Hoa",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8839-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Sơ Mi Xanh Sọc Trắng Vàng",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8428-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Sơ Mi Caro Cam Xanh",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2018/10/8S26-1-600x943.png"         
#     },
#     {
#         "title" : "Áo Sơ Mi Caro Xanh Vàng",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2018/10/IMG_2023-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Khoác Dù Nón Xám Phối Trắng",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/06/8-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Khoác Dù Nón Đen Phối Xanh",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/07/7-2-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Khoác Dù Nón Xanh Phối Đen",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/07/6-2-600x943.jpg"         
#     },
#     {
#         "title" : "Áo Khoác Dù Đen Phối 3 Sọc",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/07/áo-khoác-1-600x943.jpg"         
#     },
#     {
#         "title" : "Quần Jean Xanh Trơn",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/DSC05809-600x943.jpg"         
#     },
#     {
#         "title" : "Quần Jean Xám Wash",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/10/DSC05080-600x943.jpg"         
#     },
#     {
#         "title" : "Quần Jean Xanh Xước",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8059-600x943.jpg"         
#     },
#     {
#         "title" : "Quần Jean Xanh Rách In Chữ",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8556-600x943.jpg"         
#     },
#     {
#         "title" : "Quần Jean Trắng Trơn",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/09/DSC8402-2.jpg"         
#     },
#     {
#         "title" : "Quần Jean Xanh Nhạt",
#         "image" : "https://www.celeb.vn/wp-content/uploads/2019/07/9Q09-3-1-600x943.jpg"         
#     },
#     {
#         "title" : "Áo khoác bò",
#         "image" : "https://www.dhresource.com/0x0/f2/albu/g6/M01/84/F9/rBVaSFpwW_eAec8hAAiiIC7VsAo210.jpg"         
#     },
#     {
#         "title" : "Áo gió nam",
#         "image" : "//product.hstatic.net/1000289385/product/mausac-be_23053be6_358a7db43b4e4843a51ac7c12f158537_large.jpg"         
#     },
#     {
#         "title" : "ÁO khoác nam KAZUKI KIMONO ",
#         "image" : "//product.hstatic.net/1000289385/product/mausac-xam_23049gr1_bd3e74b855bc41cc93c6b6784b4eb6bc_large.jpg"         
#     },


# ]

# for i in list_man:
#     clother = Mancloth( title = i["title"],
#                          image = i["image"],
#                          price = randint(150000,500000),
                        
#     )
#     clother.save()

# cloth = Mancloth.objects()
# for i in cloth:    
#     print(i['id'])  // get all id from collection