# null 오류를 방지하기 위해서 빈칸을 찍어줌
class CmmUtil():
    def nvl2(pStr, chgStr):

        if pStr is None:
            return chgStr
        else:
            return pStr

    def nvl(pStr):
        return CmmUtil.nvl2(pStr, "")