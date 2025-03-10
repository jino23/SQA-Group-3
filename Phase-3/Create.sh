for i in {1..4}
do
    echo "Running test case $i..."
    python phase3_cmdlinearg.py "Create_test_cases/Create_test_run_files/Create_Input_test_run/Create_${i}_INP.txt" "Create_${i}_OUT.txt"
done

echo "All test cases completed."
