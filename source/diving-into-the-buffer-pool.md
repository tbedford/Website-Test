# Diving into the buffer pool

Some quick notes on buffer pools...

The need for buffer pools. If you have a memory constrained system and
multiple processes or even interrupt routines are running you might
get a situation where memory is monopolized by one particular
sub-system. For example, if you get a lot of packets arriving they may
quickly use up memory if the network stack is not able to process them
quickly enough. They would be buffered up, using available
memory. Then if the disk sub-system wanted memory it would not be
able to receive any, as memory has become exhausted by the incoming
packets. As the packets cannot be processed due to a lack of available
memory for disk sub-system, you have a deadlock. In addition incoming
packets will be lost as there are no buffers available for them.
  
Buffer pools can be allocated for use by a particular sub-system. The
buffers in the buffer pool are of fixed size and there is a limit on
the number of buffers in a buffer pool. When you create a buffer pool
you can specify the number of buffers (up to a hard-coded maximum),
and a buffer size (up to a hard-coded maximum). The size and number of
buffers will be sub-system-specific. 

Once a buffer pool has been created, the size of buffers in it, and
the number of buffers in it, cannot be changed in order to prevent the
sub-system monopolizing memory. 

So what happens if a sub-system exhausts the buffers in its pool? At
this point the sub-system would have to block (if network packets are
still incoming they will be lost unfortunately as they cannot be
buffered). However, the other sub-systems, such as the protocol stack,
would be able to process the data already in the sub-system's buffer
pool, freeing up buffers over time. The sub-system would at some point
then be able to continue to receive packets. 

The main point is a deadlock has not been reached, as the memory
hungry sub-system that exhausted its buffer pool would be blocked to
prevent deadlocking the other sub-systems due to memory starvation.
