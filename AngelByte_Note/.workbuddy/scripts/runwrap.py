import sys, traceback
sys.path.insert(0, r'D:\MyNotes\AngelByte_Note\.workbuddy\scripts')
out_path = r'C:\Users\29074\Desktop\out.txt'
err_path = r'C:\Users\29074\Desktop\err.txt'
with open(out_path, 'w', encoding='utf-8') as fout, open(err_path, 'w', encoding='utf-8') as ferr:
    fout.write('starting...\n')
    fout.flush()
    try:
        import build_javase as b
        fout.write('imported\n')
        fout.flush()
        b.build()
        fout.write('done\n')
        fout.flush()
    except SystemExit as e:
        ferr.write(f'SystemExit: {e}\n')
    except BaseException:
        ferr.write(traceback.format_exc())
