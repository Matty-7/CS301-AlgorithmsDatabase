import drawtree, rIO
sx = str([1, 13, 15, '(0)', 6, 14, 15, 8])
s = drawtree.draw_level_order2(sx) 
tx = str([1, 13, 15,8, 6, 14, 15, '(0)'])
t = drawtree.draw_level_order2(tx) 
print (rIO.concat_text_block(s,t,'''MAX_HEAPIFY(3)
heapsize=8'''))