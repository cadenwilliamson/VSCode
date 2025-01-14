#include <clay.h>

// Note: malloc is only used here as an example, any allocator that provides
// a pointer to addressable memory of at least totalMemorySize will work
uint64_t totalMemorySize = Clay_MinMemorySize();
Clay_Arena arena = Clay_CreateArenaWithCapacityAndMemory(totalMemorySize, malloc(totalMemorySize));
Clay_Initialize(arena, (Clay_Dimensions) { screenWidth, screenHeight });