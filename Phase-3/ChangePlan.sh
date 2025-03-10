for i in {1..5}
do
    echo "Running test case $i..."
    python phase3_cmdlinearg.py "ChangePlan_test_cases/ChangePlan_test_run_files/ChangePlan_Input_test_run/ChangePlan_${i}_INP.txt" "ChangePlan_${i}_OUT.txt"
done

echo "All test cases completed."
