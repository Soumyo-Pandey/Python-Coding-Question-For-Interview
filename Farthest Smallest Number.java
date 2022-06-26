class gfgProgram //Find The Farthest Smallest Number
{
  static int[] farNumber(int n, int arr[])
  {
      int[] arr_min = new int[n];
      arr_min[n-1] = arr[n-1];
      for (int i = n-2; i >= 0; i--)
      {
          arr_min[i] = Math.min(arr_min[i+1], arr[i]);
      }
      for (int i = 0; i < n; i++)
      {
          int low = i-1, high = n-1, val = -1;
          while(low <= high)
          {
              int mid = low + (high-low)/2;
              if(arr_min[mid] < arr[i])
              {
                  val = mid;
                  low = mid + 1;
              }
              else  {
                  high = mid -1;
              }
          }
          arr_min[i] = val;
      }
      return arr_min;
  }
}
