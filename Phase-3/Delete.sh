for i in {1..5}
do
    echo "Running test case $i..."
    python phase3_cmdlinearg.py "Delete_test_cases/Delete_test_run_files/Delete_Input_test_run/Delete_${i}_INP.txt" "Delete_${i}_OUT.txt"
done

echo "All test cases completed."
