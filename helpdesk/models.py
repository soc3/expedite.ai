from django.db import models

# Create your models here.

# constants

ISSUE_STATUSES = {
    'open': 1,
    'closed': 2,
    'archived': 3
}

ISSUE_CATEGORIES = {
    "where is my order": 1,
    "problem with an order": 2,
    "return and refunds": 3,
    "change or cancel order": 4,
    "payment issues": 5,
    "seller issues": 6,
    "delivery issues": 7,
    "promotions and deals": 8,
    "more order issues": 9
}


class Order(models.Model):
    '''An order made on the portal
    '''
    order_id = models.CharField(primary_key=True, max_length=20)
    item_name = models.CharField(null=False, blank=False, max_length=50)
    amount = models.FloatField(null=False, blank=False)
    buyer = models.CharField(null=False, blank=False, max_length=50)


class Issue(models.Model):
    '''An issue created from any comment
    '''
    ISSUE_STATUS = (
        (value, key) for key, value in ISSUE_STATUSES.items()
    )

    comment_id = models.CharField(max_length=50, primary_key=True)
    status = models.IntegerField(choices=ISSUE_STATUS)
    message = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    from_name = models.CharField(max_length=50)
    from_id = models.CharField(max_length=50)
    priority = models.IntegerField()


    def to_json(self):
        return {
            'comment_id': self.comment_id,
            'status': self.status,
            'message': self.message,
            'category': self.category,
            'created_at': self.created_at.isoformat(),
            'from_name': self.from_name,
            'from_id': self.from_id,
            'priority': self.priority
        }

    def __str__(self):
        return self.comment_id


class Reply(models.Model):
    '''Replies to an issue
    '''
    comment_id = models.CharField(max_length=50, primary_key=True)
    issue = models.ForeignKey(Issue)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    from_name = models.CharField(max_length=50)
    from_id = models.CharField(max_length=50)

    def to_json(self):
        return {
            'comment_id': self.comment_id,
            'message': self.message,
            'created_at': self.created_at,
            'from_name': self.from_name,
            'from_id': self.from_id
        }

    def __str__(self):
        return self.comment_id
