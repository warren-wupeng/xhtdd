from dataclasses import dataclass

from args.main import Args, option


class TestArgs:
    """
    我们中的大多数人都不得不时不时地解析一下命令行参数。
    如果我们没有一个方便的工具，那么我们就简单地处理一下传入 main 函数的字符串数组。
    有很多开源工具可以完成这个任务，但它们可能并不能完全满足我们的要求。所以我们再写一个吧。　
    传递给程序的参数由标志和值组成。标志应该是一个字符，前面有一个减号。
    每个标志都应该有零个或多个与之相关的值。
    例如：　-l -p 8080 -d /usr/logs　
    “l”（日志）没有相关的值，它是一个布尔标志，如果存在则为 true，不存在则为 false。
    “p”（端口）有一个整数值，
    “d”（目录）有一个字符串值。
    标志后面如果存在多个值，则该标志表示一个列表：　-g this is a list -d 1 2 -3 5　
    "g"表示一个字符串列表[“this”, “is”, “a”, “list”]，
    “d"标志表示一个整数列表[1, 2, -3, 5]。　
    如果参数中没有指定某个标志，那么解析器应该指定一个默认值。
    例如，false 代表布尔值，0 代表数字，”"代表字符串，[]代表列表。
    如果给出的参数与模式不匹配，重要的是给出一个好的错误信息，准确地解释什么是错误的。　
    确保你的代码是可扩展的，即如何增加新的数值类型是直接和明显的。
    """
    # -l -p 8080 -d /usr/logs
    # step1 确定API的形式


    # -g this is a list -d 1 2 -3 5
    def _test_should_example2(self):
        @dataclass
        class ListOptions:
            group: list[option(str, 'g')]
            decimals: list[option(int, 'd')]

        listOptions = Args.parse(
            ListOptions,
            '-g', 'this', 'is', 'a', 'list', '-d', '1', '2', '-3', '5'
        )
        assert listOptions.group == ['this', 'is', 'a', 'list']
        assert listOptions.decimals == [1, 2, -3, 5]
    # step2 大致构思实现方式
    #
    # [-l], [-p, 8080], [-d, /usr/logs]
    # single option:

    def test_should_set_boolean_option_to_true_if_flag_present(self):
        @dataclass
        class BooleanOption:
            logging: option(bool, "l")
        BoolOption = Args.parse(BooleanOption, "-l")
        assert BoolOption.logging is True

    def test_should_set_boolean_option_to_false_if_flag_not_present(self):
        @dataclass
        class BooleanOption:
            logging: option(bool, "l")
        BoolOption = Args.parse(BooleanOption)
        assert BoolOption.logging is False

    def test_should_parse_int_as_option_value(self):
        @dataclass
        class IntOption:
            port: option(int, "p")

        intOption = Args.parse(IntOption, "-p", "8080")
        assert intOption.port == 8080

    def test_should_get_string_as_option_value(self):
        @dataclass
        class StringOption:
            directory: option(str, "d")

        strOption = Args.parse(StringOption, "-d", "/usr/logs")
        assert strOption.directory == '/usr/logs'

    # TODO: multi options: -l -p 8080 -d /usr/logs
    def test_should_parse_multi_options(self):
        @dataclass
        class MultOptions:
            logging: option(bool, 'l')
            port: option(int, 'p')
            directory: option(str, 'd')

        options = Args.parse(MultOptions, "-l", "-p", "8080", "-d", "/usr/logs")
        assert options.logging is True
        assert options.port == 8080
        assert options.directory == "/usr/logs"
    # sad path:
    # TODO: - bool -l t / -l t f
    # TODO: - int -p/ -p 8080 8081
    # TODO: - string -d/ -d /usr/logs /usr/vars
    # default value:
    # TODO: - bool : false
    # TODO: - int: 0
    # TODO: - string ""






