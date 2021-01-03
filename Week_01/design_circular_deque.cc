#include <iostream>
#include <vector>

using namespace std;

class MyCircularDeque {
private:
  int cap;
  int count;
  int front_idx;
  int rear_idx;
  vector<int> data;
public:
  MyCircularDeque(int k) {
    cap = k;
    data = vector<int>(k);
    count = 0;
    front_idx = k - 1;
    rear_idx = 0;
  }

  bool insertFront(int value) {
    if (count == cap) return false;
    data[front_idx] = value;
    front_idx = (front_idx - 1 + cap) % cap;
    count++;
    return true;
  }

  bool insertLast(int value) {
    if (count == cap) return false;
    data[rear_idx] = value;
    rear_idx = (rear_idx + 1) % cap;
    count++;
    return true;
  }

  bool deleteFront() {
    if (count == 0) return false;
    front_idx = (front_idx + 1) % cap;
    count--;
    return true;
  }

  bool deleteLast() {
    if (count == 0) return false;
    rear_idx = (rear_idx - 1 + cap) % cap;
    count--;
    return true;
  }

  int getFront() {
    return count == 0 ? -1 : data[(front_idx + 1) % cap];
  }

  int getRear() {
    return count == 0 ? -1 : data[(rear_idx - 1 + cap) % cap];
  }

  bool isEmpty() {
    return count == 0;
  }

  bool isFull() {
    return count == cap;
  }
};

/*
int main() {
  MyCircularDeque dq = MyCircularDeque(3);
  cout << dq.insertLast(1) << endl;
  cout << dq.insertLast(2) << endl;
  cout << dq.insertFront(3) << endl;
  cout << dq.insertFront(4) << endl;
  cout << dq.getRear() << endl;
  cout << dq.isFull() << endl;
  cout << dq.deleteLast() << endl;
  cout << dq.insertFront(4) << endl;
  cout << dq.getFront() << endl;
}
*/
