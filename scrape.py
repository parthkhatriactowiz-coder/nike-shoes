import json, os


def read_json_file(file_path):
    with open(file_path, "r") as f:
        return json.loads(f.read())

data = read_json_file(
    "C:/Users/parth.khatri/Desktop/github/nike-shoes/nyka.json"
)

base_url = "https://www.nykaaman.com/"
product_data = []

variants = data.get("productPage", {}).get("product", {}).get("variants", [])
parent_id = data.get("productPage", {}).get("product", {}).get("parentId", "")
rating = data.get("productPage", {}).get("product", {}).get("rating", "")
rating_count = data.get("productPage", {}).get("product", {}).get("ratingCount", "")
offers = data.get("productPage", {}).get("product", {}).get("offers", [])
coupon_offers = data.get("couponReducer", {}).get("coupons", {}).get("data", [])  

for product in variants:
    product_info = {}

    product_info["brand_name"] = product.get("brandName", "")

    product_url = f"{base_url}{product.get('slug', '')}?productId={parent_id}&skuId={product.get('childId', '')}"
    product_info["url"] = product_url

    product_info["id"] = product.get("sku", "")
    product_info["name"] = product.get("name", "")
    product_info["rating"] = float(rating) if rating != "" else ""                 
    product_info["rating_count"] = rating_count
    product_info["main_image"] = product.get("imageUrl", "")

    # other_images = product.get("media", [])
    # print(other_images,"other_images")
    # for media in other_images:
    #     product_info["other_images"] = media.get("url", "")

    product_info["other_images"] = []
    for media in product.get("media", []):
        product_info["other_images"].append(media.get("url", ""))

    product_info["price"] = float(product.get("offerPrice", 0))                  
    product_info["discount"] = float(product.get("discount", 0))                         
    product_info["original_price"] = float(product.get("mrp", 0))                    
    
    coupon_list = []
    for coupon in coupon_offers:
        coupon_list.append(str(coupon))
    product_info["coupon_offers"] = coupon_list
    product_data.append(product_info)

output_path = "C:/Users/parth.khatri/Desktop/github/nike-shoes/nykaa_output.json"
with open(output_path, "w") as f:
    json.dump(product_data, f, indent=4)
