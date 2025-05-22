# 정답 제출 형식
1. **파이썬**만 사용
2. **외부 패키지 사용 금지**
3. 파일 이름
    - `<깃헙 아이디>_<문제 이름>.py`
    - 예: `kmsrogerkim_Two_Sum.py`
4. I/O 처리
    - 별도로 I/O 처리 하지 않고, 코드에 테스트 변수 하드코딩
    ```python
    def whatever(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []

    def main():
        inpt: List[int] = [1,2,3,4]
        target: int = 3
        ans: int = whatever(inpt, target)
        print(ans)
    ```