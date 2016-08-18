# Set up basic variables:
CC = clang
CFLAGS = -c -Wall -std=c++11 -g
LDFLAGS = -lc++

# List of sources:
SOURCES = show_img.cpp
OBJECTS = $(SOURCES:.cpp=.o)
# Name of executable target:
EXECUTABLE = show_img

# Here we invoke "pkg-config" passing it as argument the list of the
# OpenCV libraries needed by our program.
#
export PKG_CONFIG_PATH=/usr/local/opt/opencv3/lib/pkgconfig
CFLAGS += `pkg-config --cflags opencv`
LDFLAGS += `pkg-config --libs opencv`
LDFLAGS += -L/usr/local/opt/opencv3/share/OpenCV/3rdparty/lib

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@ $(LDFLAGS)

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm $(OBJECTS) $(EXECUTABLE)
