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
	int startx0, starty0, width0, height0, displayStart;
    int y,x;
    int count;
    char msg[50];
	int ch;

	initscr();			/* Start curses mode 		*/
	cbreak();			/* Line buffering disabled, Pass on everty thing to me 		*/
					 
    height0 = 3;
    width0 = COLS - 2;
    starty0 = LINES - height0;	/* Calculating for a center placement */
    startx0 = (COLS - width0) / 2;	/* of the window		*/

    int pad_height = 50, pad_width = width0;    //pad_height set 50 for testing, will crank it up later
    int display_height = LINES - height0-1, display_width = width0;
    displayPad = newpad(pad_height, pad_width);
    if (!displayPad) {
        endwin();
        fprintf(stderr, "Failed to create pad\n");
        return 1;
    }



    my_win = create_newwin(height0, width0, starty0, startx0);

    //displayPad = create_newwin(6, width0, 1, 1);
    displayStart = 1;

    
    while(1){
        mvwprintw(my_win, 1,2, ": ");
        mvwgetstr(my_win,1,3,  msg);
        wmove(my_win, 1, 4);
        wclrtoeol(my_win);
        box(my_win, 0, 0);


        mvwprintw(displayPad, displayStart,2, msg);
        prefresh(displayPad, pad)
        displayStart ++;

        //refresh();
        //wrefresh(my_win);		/* Show that box 		*/
    }
    ch = getch();
		
    delwin(displayPad);
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