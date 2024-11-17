class House:
    def __init__(self, style):
        self.style = style
        self.parts = {}

    def __str__(self):
        features = [f"Style: {self.style}"]
        for part, material in self.parts.items():
            features.append(f"{part.capitalize()}: {material}")

        return ", ".join(features)


class HouseBuilder:
    def __init__(self, style):
        self.house = House(style)

    def build_part(self, part, material):
        self.house.parts[part] = material
        return self

    def build(self):
        return self.house


class SummerHouseBuilder(HouseBuilder):
    def __init__(self):
        super().__init__("Summer House")
        self.build_part("walls", "Wood")
        self.build_part("roof", "Thatch")
        self.build_part("foundation", "Wooden")


class UrbanHouseBuilder(HouseBuilder):
    def __init__(self):
        super().__init__("Urban House")
        self.build_part("walls", "Brick")
        self.build_part("roof", "Concrete")
        self.build_part("foundation", "Concrete")


# Пример использования
if __name__ == "__main__":
    summer_house_builder = SummerHouseBuilder()
    summer_house = (summer_house_builder
                    .build_part("garage", "Detached")
                    .build_part("pool", "Oval")
                    .build())

    print(summer_house)
    # Style: Summer House, Walls: Wood, Roof: Thatch, Foundation: Wooden, Garage: Detached, Pool: Oval

    print("\n-----------------\n")

    urban_house_builder = UrbanHouseBuilder()
    urban_house = (urban_house_builder
                   .build_part("garage", "Attached")
                   .build_part("pool", "Square")
                   .build())

    print(urban_house)
    # Style: Urban House, Walls: Brick, Roof: Concrete, Foundation: Concrete, Garage: Attached, Pool: Square
