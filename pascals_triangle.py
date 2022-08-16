from re import L
from tkinter import N


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        row=[1]
        triangle= self.generate(numRows-1)
        last_row=triangle[-1]
        for i in range(len(last_row)-1):
            num=last_row[i]+last_row[i+1]
            row.append(num)
        row.append(1)
        triangle.append(row)

        return triangle                 