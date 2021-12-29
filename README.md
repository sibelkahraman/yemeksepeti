# yemeksepeti

Online food ordering become very important day by day in human life.

Wide range of food, quick delivery, easy to use are key points.

Here at Yemeksepeti Elements:
- User: Who gives an order from foods.
- Food: That has category and ingredients for different type of.
- Restaurant: That has foods.
- Order: That has a list of food from a restaurant is ordering from a user.
- Ingredient: That is one of the substances of a food.
- Category: That is class of food.
- Address: That is address of restaurant or user.



For any CRUD operation on the element is operated over API.

When a order is created over thi API, the order is added into a queue.

The order waits until ***/complete*** endpoint get a request.

After the request status of the order become completed and ready to deliver.

