class Matrix //Coils Of a Matrix
{
  static int[][] fromcoils(int n)
  {
      int m = 8*n*n;
      int [][] mat = new int [2][m];
      mat[0][0] = 8*n*n+2*n;
      int ele = mat[0][0], direction = 1, step = 2, i = 1;
      while(i<m)
      {
          for(int j=0; j<step; j++)
          {
              ele = mat[0][i+1] = (ele-4*n*direction);
              if(i>=m)
              break;
          }
          if(i>=m)
          break;
          for(int j=0; j<step; j++)
          {
              ele = mat[0][i++] = ele + direction;
              if(i>=m)
              break;
          }
          direction*=-1;
          step+=2;
      }
      for(int k=0; k<m; k++)
      {
          mat[i][k] = 16*n*n+1 - mat[0][k];
      }
      return mat;
  }
}
