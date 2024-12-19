#include <ncurses.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <string.h>

WINDOW *create_newwin(int height, int width, int starty, int startx);

int main(int argc, char *argv[])
{	WINDOW *my_win, *displayPad;
	int startx0, starty0, width0, height0;
    int leftx, lefty, rightx, righty;
    int y,x;
    int count;
    char msg[50];
	int ch;

	initscr();			/* Start curses mode 		*/
	cbreak();			/* Line buffering disabled, Pass on
					 * everty thing to me 		*/


    height0 = 3;
    width0 = COLS - 2;
    starty0 = LINES - height0;	/* Calculating for a center placement */
    startx0 = (COLS - width0) / 2;	/* of the window		*/
    



    my_win = create_newwin(height0, width0, starty0, startx0);
        mvwprintw(my_win, 1,2, ": ");

        box(my_win, 0, 0);

        refresh();
        //wrefresh(my_win);		/* Show that box 		*/

    ch = getch();
		
	endwin();			/* End curses mode		  */
	return 0;
}

WINDOW *create_newwin(int height, int width, int starty, int startx)
{	WINDOW *local_win;

	local_win = newwin(height, width, starty, startx);
    box(local_win, 0, 0);
	wrefresh(local_win);		/* Show that box 		*/

	return local_win;
}