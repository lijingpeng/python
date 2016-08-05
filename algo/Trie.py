#!/usr/bin/python
# -*- encoding: UTF-8 -*-
import codecs

class TrieNode(object):
    '''
    Trie Node定义
    '''
    def __init__(self):
        self.val = 0
        self.trans = {}

class Trie(object):
    '''
    Trie 树
    '''
    def __init__(self):
        self.root = TrieNode()

    def _walk(self, trienode, ch):
        if ch in trienode.trans:
            trienode = trienode.trans[ch]
            return trienode, trienode.val
        else:
            return None, 0

    def add(self, word, value=1):
        '''
        向树中添加词
        '''
        curr_node = self.root
        for ch in word:
            try:
                curr_node = curr_node.trans[ch]
            except:
                curr_node.trans[ch] = TrieNode()
                curr_node = curr_node.trans[ch]

        curr_node.val = value


    def _find_ch(self, curr_node, ch, word, start, limit):
        curr_node, val = self._walk(curr_node, ch)
        if val:
            return val
        while curr_node is not None and start < (limit-1):
            start = start + 1
            ch = word[start]
            curr_node, val = self._walk(curr_node, ch)
            if val:
                return val

    def match_all(self, word):
        '''
        匹配所有关键词
        '''
        ret = []
        curr_node = self.root
        index = 0
        size = len(word)
        while index < size:
            val = self._find_ch(curr_node, word[index], word, index, size)
            if val:
                ret.append(val)
            index = index+1
        return ret

class Dict(Trie):
    '''
    Dict
    '''
    def __init__(self, fname):
        super(Dict, self).__init__()
        self.load(fname)

    def load(self, fname):
        '''
        载入词典
        :param fname: 文件名
        :return: 无
        '''
        f = codecs.open(fname, 'r', 'utf-8')
        for line in f:
            word = line.strip()
            self.add(word, word)
        f.close()

if __name__ == "__main__":
    local_dict = Dict("/Users/frank/dict.dic")
    test_str = u"大庆让胡路喇嘛甸哪里有找小姐服务１８６－５５５５－２５５７娜娜【ＱＱ１９６８４５４６８８空间选小姐】哪里有小姐服务" \
               u"１８６－５５５５－２５５７【ＱＱ１９６８４５４６８８空间选小姐】哪里有小姐服务１８６－５５５５－２５５７娜娜【ＱＱ１９６８４５４６８８空间" \
               u"看照片】无论朋友你常住本市。。 哪里找小姐服务娜娜【１８６－５５５５－２５５７娜娜】还是阁下才来我市。这些都" \
               u"不重要。。哪里找小姐服务１８６－５５５５－２５５７娜娜因为找我们在寂寞的深夜你不在感到孤单和寂寞。。"
    ret = local_dict.match_all(test_str)
    print " ".join(ret)
