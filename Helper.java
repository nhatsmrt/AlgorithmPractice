class Helper {
  private static void printArray(int[][] arr) {
      String rep = "[";
      for (int i = 0; i < arr.length; i++) {
          String subarr = "[";
          for (int j = 0; j < arr[0].length; j++) {
              subarr += arr[i][j];
              if (j < arr[0].length - 1)
                  subarr += ", ";
          }
          subarr += "]";
          rep += "" + subarr;
          if (i < arr.length - 1)
              rep += ", ";
      }
      rep += "]";
      System.out.println(rep);
  }
}
