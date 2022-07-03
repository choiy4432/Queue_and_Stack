# Queue_and_Stack

Queue(Stack) 2개를 사용하여 Stack(Queue) 구현

stack 으로 Queue를 구현하기 위해 2개의 stack, 그리고 queue 로 Stack을 구현하기 위해 2개의 queue를 사용하였다. Stack 과 queue 는 입력받은 item 을 제거하는 방식을 동일하지만, item을 입력하는 방법이 다르다. Stack의 경우는 LIFO 구조로, 입력받은 item이 마지막에 저장되고, item을 제거할때도 마지막으로 입력받은 item을 제거한다. 반면 queue의 경우 FIFO구조로, 입력받은 item이 제일 앞에 저장되고, item을 제거할때는 처음으로 입력받은 item 부터 제거하게 된다. 두 가지 형식의 경우 서로 item을 입력할때 순서를 반대로 하면 되기 때문에 이를 구현할 때, item의 순서를 swap하는 식, 즉 queue 에서의 마지막 item을 stack의 첫번째 item으로, stack의 마지막 item을 queue의 첫번째 item으로 저장하면 완벽히 stack 과 queue가 구현이 된다.
