#include <ncurses.h>
#include <stdlib.h>
#include <string.h>

#define MSG_LEN_LIMIT 256

int main() {
    char *msg = calloc(MSG_LEN_LIMIT, sizeof(char));
    // Initialize ncurses
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);

    int rows, cols, writeLine;
    getmaxyx(stdscr, rows, cols);

    // Create a pad
    int pad_height = 100;
    int pad_width = cols - 2;
    WINDOW *pad = newpad(pad_height, pad_width);
    if (pad == NULL) {
        endwin();
        fprintf(stderr, "Error creating pad\n");
        exit(1);
    }

    // Fill the pad with content

    // for (int i = 0; i < pad_height; i++) {
    //     mvwprintw(pad, i, 0, "%s %d", "helo", i); // Fill with letters
    // }

    // Display part of the pad
    int pad_top = 0;
    int pad_left = 0;
    int visible_height = rows - 2;
    int visible_width = cols - 2;

    mvprintw(rows - 1, 0, "type 'a' for messaging , 'q' to quit: ");
    refresh();

    writeLine = 0;
    // Handle user input for scrolling
    int ch;
    while ((ch = getch()) != 'q') {
        switch (ch) {
            case KEY_UP:
                if (pad_top > 0) pad_top--;
                break;
            case KEY_DOWN:
                if (pad_top + visible_height < pad_height) pad_top++;
                break;
            // case KEY_LEFT:
            //     if (pad_left > 0) pad_left--;
            //     break;
            // case KEY_RIGHT:
            //     if (pad_left + visible_width < pad_width) pad_left++;
            //     break;
            case 'a':
                echo();
                move(rows-1, 0);
                clrtoeol();
                refresh();
                mvprintw(rows - 1, 0, ":");
                mvgetstr(rows - 1, 2,  msg);
                //integrate the first letter to rest of msg
                mvwprintw(pad, writeLine, 0, "me: %s", msg);
                clrtoeol();
                refresh();
                noecho();
                writeLine++;
                move(rows-1, 0);
                if (writeLine > visible_height) pad_top++;
                break;
            default:
                break;
        }

        // Display the pad content within the visible window
        prefresh(pad, pad_top, pad_left, 0, 0, visible_height, visible_width);
    }
    free(msg);
    // Cleanup
    delwin(pad);
    endwin();
    return 0;
}
