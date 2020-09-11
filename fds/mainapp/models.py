from django.db import models
# Models.oy file
ROLE_CHOICE = (
    ('admin', 'Admin'),
    ('buyer', 'Buyer')
)


class Reg_user(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(max_length=100)
    passowrd = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to='profile_picture')
    address = models.TextField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    role = models.CharField(
        max_length=100, choices=ROLE_CHOICE, default='buyer')
    status = models.CharField(max_length=100)

    class Meta:
        db_table = "reg_user"


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    mobile_number = models.IntegerField()
    pincode = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    description = models.TextField(default="None")
    logo = models.ImageField(upload_to='res_logo')
    status = models.CharField(max_length=100)
    cuisine_name = models.CharField(max_length=100, default="None")
    price_for_two = models.IntegerField(default="0")

    class Meta:
        db_table = "restaurant"


class Delivery_agent(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to='d_profilepicture',default="None")
    address = models.TextField()
    pincode = models.IntegerField()
    status = models.CharField(max_length=100)
    

    class Meta:
        db_table = "delivery_agent"


class Ambience(models.Model):
    photos = models.ImageField(upload_to='ambience_photos')
    status = models.CharField(max_length=100, default='Not Verified')
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = "ambience"


class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=100)
    cuisine_photo = models.ImageField(upload_to='cuisine_photos')

    class Meta:
        db_table = "cuisine"


class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    price = models.IntegerField()
    dish_description = models.TextField(max_length=100)
    dish_photo = models.ImageField(upload_to='dish_photos/')
    customization = models.CharField(max_length=100)
    cuisine_id = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = "dish"


class Discount(models.Model):
    discount_value = models.IntegerField()
    discount_description = models.TextField()
    discount_limit = models.IntegerField()
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = "discount"


class Cart(models.Model):
    total_amount = models.FloatField()
    status = models.CharField(max_length=100)
    reg_user_id = models.ForeignKey(Reg_user, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE)

    class Meta:
        db_table = "cart"


class Order(models.Model):
    total_amount = models.FloatField()
    payment_type = models.CharField(max_length=100)
    order_date = models.DateField()
    order_time = models.DateTimeField()
    status = models.CharField(max_length=100)
    reg_user_id = models.ForeignKey(Reg_user, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(Delivery_agent, on_delete=models.CASCADE)

    class Meta:
        db_table = "order"


class Food_rating(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    reg_user_id = models.ForeignKey(Reg_user, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        db_table = "food_rating"


class Agent_rating(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    reg_user_id = models.ForeignKey(Reg_user, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(Delivery_agent, on_delete=models.CASCADE)

    class Meta:
        db_table = "agent_rating"


class Verification(models.Model):
    shop_fssai_license = models.ImageField(upload_to="verification_photos")
    pan_card = models.ImageField(upload_to="verification_photos")
    gst_number = models.CharField(max_length=100, null=True, blank=True)
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = "verification"


class Report(models.Model):
    report_type = models.CharField(max_length=100, null=True, blank=True)
    report_subject = models.CharField(max_length=100, null=True, blank=True)
    report_date = models.DateTimeField(max_length=100)
    report_message = models.CharField(max_length=100, null=True, blank=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = "report"
