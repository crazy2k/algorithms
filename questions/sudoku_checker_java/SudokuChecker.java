import java.util.Set;
import java.util.HashSet;

public class SudokuChecker {
	
	public static boolean check(int[][] sudoku) {
		return SudokuChecker.checkRows(sudoku) &&
				SudokuChecker.checkCols(sudoku) &&
				SudokuChecker.checkSquares(sudoku);
	}
	
	private static Set<Integer> digitsSet() {
		Set<Integer> s = new HashSet<Integer>();
		for (int i = 0; i < 10; i++) {
			s.add(i);
		}
		return s;
	}
	
	public static boolean checkRows(int[][] sudoku) {
		for (int i = 0; i < sudoku.length; i++) {
			Set<Integer> s = SudokuChecker.digitsSet();
			for (int j = 0; j < sudoku.length; j++) {
				if (!s.remove(sudoku[i][j]))
					return false;
			}
		}
		return true;
	}

	public static boolean checkCols(int[][] sudoku) {
		for (int j = 0; j < sudoku.length; j++) {
			Set<Integer> s = SudokuChecker.digitsSet();
			for (int i = 0; i < sudoku.length; i++) {
				if (!s.remove(sudoku[i][j]))
					return false;
			}
		}
		return true;
	}
	
	public static boolean checkSquare(int[][] sudoku, int i, int j) {
		Set<Integer> s = SudokuChecker.digitsSet();
		for (int ioffset = 0; ioffset < 3; ioffset++)
			for (int joffset = 0; joffset < 3; joffset++)
				if (!s.remove(sudoku[i + ioffset][j + joffset]))
					return false;
		return true;
	}
	
	public static boolean checkSquares(int[][] sudoku) {
		for (int i = 0; i < sudoku.length; i += 3) {
			for (int j = 0; j < sudoku.length; j += 3) {
				if (!SudokuChecker.checkSquare(sudoku, i, j))
					return false;
			}
		}
		return true;
	}
}