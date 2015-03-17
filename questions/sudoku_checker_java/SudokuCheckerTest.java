import static org.junit.Assert.*;

import org.junit.Test;


public class SudokuCheckerTest {

	@Test
	public void testCorrect() {
		int[][] sudoku = new int[][] {
			{1, 4, 5, 3, 2, 7, 6, 9, 8},
			{8, 3, 9, 6, 5, 4, 1, 2, 7},
			{6, 7, 2, 9, 1, 8, 5, 4, 3},
			{4, 9, 6, 1, 8, 5, 3, 7, 2},
			{2, 1, 8, 4, 7, 3, 9, 5, 6},
			{7, 5, 3, 2, 9, 6, 4, 8, 1},
			{3, 6, 7, 5, 4, 2, 8, 1, 9},
			{9, 8, 4, 7, 6, 1, 2, 3, 5},
			{5, 2, 1, 8, 3, 9, 7, 6, 4}
		};
		assertTrue(SudokuChecker.check(sudoku));
	}
	
	@Test
	public void testIncorrect() {
		int[][] sudoku = new int[][] {
			{1, 4, 5, 3, 2, 7, 6, 9, 8},
			{8, 3, 9, 6, 5, 4, 1, 2, 7},
			{6, 7, 2, 9, 1, 8, 5, 4, 3},
			{4, 9, 6, 1, 8, 5, 3, 7, 2},
			{2, 1, 8, 4, 7, 3, 9, 5, 6},
			{7, 5, 3, 2, 9, 6, 4, 8, 1},
			{3, 6, 7, 5, 4, 2, 8, 1, 9},
			{9, 8, 4, 7, 6, 1, 2, 3, 5},
			{5, 2, 1, 8, 3, 9, 8, 6, 4}
		};
		assertFalse(SudokuChecker.check(sudoku));
	}
}