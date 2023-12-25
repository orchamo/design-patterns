from Subject import Subject
from observers.One import One
from observers.Two import Two

# creates the instances and shows that when the counter updates the observer update as well.

counter = Subject()

one = One(counter)
two = Two(counter)

counter.add(one)
counter.add(two)
counter.plus_one()
counter.plus_one()
counter.plus_one()
one.display()
two.display()