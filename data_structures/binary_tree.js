function BinaryTree(val, left, right) {
  this.val = val || 0;
  this.left = left 	|| null;
  this.right = right || null;
}
const myTree = new BinaryTree();

function mapTree(n = 5, tree) {
  tree.val = Math.floor(Math.random() * 100);
  if (n < 0) return
  tree.left = new BinaryTree();
  tree.right = new BinaryTree();
  n--;
  mapTree(n, tree.left);
  mapTree(n, tree.right);
}

mapTree(5, myTree);
console.log(JSON.stringify(myTree));
