class multifilter:
    
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg:
            return True

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1:
            return True
    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs  
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            pos = 0
            neg = 0
            for function in self.funcs:
                if function(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield i    
 