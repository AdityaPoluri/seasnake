from tests.utils import GeneratorTestCase


class FunctionTestCase(GeneratorTestCase):
    def test_empty(self):
        self.assertGeneratedOutput(
            """
            void empty() {

            }
            """,
            """
            def empty():
                pass


            """
        )

    def test_simple(self):
        self.assertGeneratedOutput(
            """
            int double_value(int in) {
                int out;

                out = in * 2;

                return out;
            }
            """,
            """
            def double_value(in):
                out = in * 2
                return out


            """
        )
