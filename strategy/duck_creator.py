from Duck import Duck
from behaviors.fly.FlyHigh import FlyHigh
from behaviors.quack.QuackLoud import QuackLoud

#creating a duck instance
danny = Duck("danny", FlyHigh(), QuackLoud())
print(danny)