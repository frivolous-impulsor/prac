#include <ncurses.h>


WINDOW *create_newwin(int height, int width, int starty, int startx);

int main(int argc, char *argv[])
{	WINDOW *my_win;
	int startx0, starty0, width0, height0;
    int y,x;
    char msg[50];
	int ch;

	initscr();			/* Start curses mode 		*/
	cbreak();			/* Line buffering disabled, Pass on
					 * everty thing to me 		*/
	keypad(stdscr, TRUE);		/* I need that nifty F1 	*/

	height0 = 3;
	width0 = COLS - 2;
	starty0 = LINES - height0;	/* Calculating for a center placement */
	startx0 = (COLS - width0) / 2;	/* of the window		*/
    



	my_win = create_newwin(height0, width0, starty0, startx0);
    while(1){
        mvwprintw(my_win, 1,2, ": ");
        mvwgetstr(my_win,1,3,  msg);
        wmove(my_win, 1, 4);
        wclrtoeol(my_win);
        wborder(my_win, '|', '|', '-', '-', '+', '+', '+', '+');

        refresh();
	    //wrefresh(my_win);		/* Show that box 		*/
    }


    ch = getch();
		
	endwin();			/* End curses mode		  */
	return 0;
}

WINDOW *create_newwin(int height, int width, int starty, int startx)
{	WINDOW *local_win;

	local_win = newwin(height, width, starty, startx);
    wborder(local_win, '|', '|', '-', '-', '+', '+', '+', '+');
	wrefresh(local_win);		/* Show that box 		*/

	return local_win;
}