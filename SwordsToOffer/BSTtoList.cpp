//BST to ListNode
TreeNode *flatten(TreeNode *root)
{
    if (!root) return;
    //
    TreeNode *searchHead = root;
    while(searchHead->left) searchHead = searchHead->left;
    TreeNode *listHead = new TreeNode();
    listHead -> right =  searchHead
    listHead -> left = NULL;
    //
    stack<TreeNode *> node_st;
    while(!node_st.empty())
    {
        TreeNode *top_node = node_st.top();
        node_st.pop();
        if(top_node->left)
        {
            node_st.push(top_node->left);
            TreeNode *tmp_l = top_node->left;
            while(tmp_l->right) tmp_l = tmp_l->right;
            tmp_l->right = top_node;
            tmp_l->left = NULL;
        }
        if(top_node->right)
        {
            node_st.push(top_node>right);
            TreeNode *tmp_r = top_node->right;
            while(tmp_r->left)tmp_r = tmp_r->left;
            top_node->right = tmp_r;
            top_node->left = NULL;
        }
    }
    return listHead;
}