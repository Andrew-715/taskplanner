import factory.django

from goals.models import Goal


class CreateGoalCategoryRequest(factory.DictFactory):
    title = factory.Faker('catch_phrase')


class CreateGoalRequest(factory.DictFactory):
    title = factory.Faker('catch_phrase')

    @classmethod
    def perform_destroy(self, instance: Goal) -> None:
        instance.status = Goal.Status.archived
        instance.save(update_fields=['status'])


# class CreateGoalCommentRequest(factory.DictFactory):
#     text = factory.Faker('sentence')
