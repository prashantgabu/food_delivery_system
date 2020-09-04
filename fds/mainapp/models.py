from django.db import models

ROLE_CHOICE = (
    ('admin', 'Admin'),
    ('buyer', 'Buyer')
)


class reg_user(models.Model):
    name = models.CharField(max_length=100)
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


class restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    mobile_number = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='profile_picture')
    status = models.CharField(max_length=100)
    cuisine_name = models.CharField(max_length=100)
    price_for_two = models.IntegerField()

    class Meta:
        db_table = "restaurant"


class delivery_agent(models.Model):
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
    docs = models.ImageField(upload_to='documents')

    class Meta:
        db_table = "delivery_agent"


class ambience(models.Model):
    photos = models.ImageField(upload_to='ambience_photos')
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = "ambience"


class cuisine(models.Model):
    cuisine_name = models.CharField(max_length=100)
    cuisine_photo = models.ImageField(upload_to='cuisine_photos')

    class Meta:
        db_table = "cuisine"


class dish(models.Model):
    dish_name = models.CharField(max_length=100)
    price = models.IntegerField()
    dish_description = models.TextField(max_length=100)
    dish_photo = models.ImageField(upload_to='dish_photos')
    customization = models.CharField(max_length=100)
    cuisine_id = models.ForeignKey(cuisine, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = "dish"


class discount(models.Model):
    discount_value = models.IntegerField()
    discount_description = models.TextField()
    discount_limit = models.IntegerField()
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = "discount"


class cart(models.Model):
    total_amount = models.FloatField()
    status = models.CharField(max_length=100)
    reg_user_id = models.ForeignKey(reg_user, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount_id = models.ForeignKey(discount, on_delete=models.CASCADE)

    class Meta:
        db_table = "cart"


class order(models.Model):
    total_amount = models.FloatField()
    payment_type = models.CharField(max_length=100)
    order_date = models.DateField()
    order_time = models.DateTimeField()
    status = models.CharField(max_length=100)
    reg_user_id = models.ForeignKey(reg_user, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(cart, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(delivery_agent, on_delete=models.CASCADE)

    class Meta:
        db_table = "order"


class food_rating(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    reg_user_id = models.ForeignKey(reg_user, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(dish, on_delete=models.CASCADE)

    class Meta:
        db_table = "food_rating"


class agent_rating(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    reg_user_id = models.ForeignKey(reg_user, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(delivery_agent, on_delete=models.CASCADE)

    class Meta:
        db_table = "agent_rating"
