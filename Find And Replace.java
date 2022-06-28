class StringFind
{
  static String findAndReplace(String s, int Q, int [] index, String[] Sources, String[] targets)
  {
      list<int[]>arr = new ArrayList<>();
      for(int i = 0; i<Q; i++)
      arr.add(new int[], {index[i], i});
  }
  collections.Sort(arr, (a,b)-> b[0] - a[0]);
  for(int[].ind:arr)
  {
      int i = ind[0], j = ind[1];
      String s = Source[j], t = targets[j];
      if(s.substring(i, i + s.length()).equals(s))
      s = s.substring(0, i) + t + s.substring(i+s.length());
  }
  return s;
}
}

