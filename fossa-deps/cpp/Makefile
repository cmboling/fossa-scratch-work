CC = gcc
CFLAGS = -Wall -Wextra -std=c99
LDFLAGS = -lm
LIB_PATH = /usr/local/lib /opt/lib
INC_PATH = /usr/local/include /opt/include

SRCS = main.c foo.c bar.c
OBJS = $(SRCS:.c=.o)
TARGET = myprogram
DEPS = lib1 lib2

%.o: %.c
    $(CC) $(CFLAGS) -I$(INC_PATH) -c $< -o $@

$(TARGET): $(OBJS)
    $(CC) $(OBJS) -L$(LIB_PATH) $(LDFLAGS) -o $(TARGET) $(addprefix -l, $(DEPS))

.PHONY: clean
clean:
    rm -f $(OBJS) $(TARGET)
