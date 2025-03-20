class Solution:
  # 1
  # 1 2
  # 2 1
  # -3 -5
  # 1 2 4 5 7 8 3
  def peakElement(self, arr):
    if len(arr) == 1:
      return 0
    for i in range(0, len(arr) - 1):
      print(f"{arr[i]} > {arr[i - 1]}")
      if arr[i] > arr[i - 1]:
        print(f"{arr[i]} > {arr[i + 1]}")
        if arr[i] > arr[i + 1]:
          print(f"Solución {arr[i]}")
          return i
      else:
        print(f"Solución {arr[i - 1]}")
        return i - 1
    print(f"Solución {arr[len(arr) - 1]}")
    return len(arr) - 1
  
Solution.peakElement(Solution, [-3, -5])