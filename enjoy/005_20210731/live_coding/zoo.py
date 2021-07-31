import animals as a
import keeper as k

dict_animals = {
        'classes': [k.keeper, a.dog, a.cat],
        'names': ['taro', 'pochi', 'mike']
        }


def feed_time(animals):
    keeper = animals[0]
    keeper.feed(animals[1])
    keeper.feed(animals[1])
    keeper.feed(animals[1])
    keeper.feed(animals[1])
    keeper.feed(animals[1])
    keeper.feed(animals[1])
    keeper.feed(animals[1])
    keeper.feed(animals[1])
    keeper.feed(animals[1])
    keeper.feed(animals[1])
    keeper.feed(animals[1])
    keeper.feed(animals[2])
    keeper.feed(animals[2])


def bark_party(animals):
    for animal in animals:
        animal.bark()


def main():
    print('this is zoo')

    animals = []
    for class_, name in zip(dict_animals['classes'], dict_animals['names']):
        animals.append(class_(name))

    # esaやり
    feed_time(animals)

    # party
    bark_party(animals)


if __name__ == '__main__':
    main()
