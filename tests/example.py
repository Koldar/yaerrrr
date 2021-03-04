import yaerrrr


class TestEr(yaerrrr.AbstractYaerrrrScript):

    def generate_er(self, context: 'yaerrrr.YaerrrContext') -> "yaerrrr.ErDiagram":
        er = context.er

        er.add_entity(name="authors", fields=[
            er.generate_primary_id_key(),
        ])
        er.add_entity(name="books", fields=[
            er.generate_primary_id_key()
        ])
        er.add_1_to_0_n("authors", "books", "writes")

        return er


def main():
    x = TestEr()
    x.run("output.svg")


if __name__ == "__main__":
    main()
