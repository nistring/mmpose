# 19 keypoints
# python demo/topdown_demo_batch.py \
#     demo/mmdetection_cfg/rtmdet_m_640-8xb32_coco-person.py \
#     https://download.openmmlab.com/mmpose/v1/projects/rtmpose/rtmdet_m_8xb32-100e_coco-obj365-person-235e8209.pth \
#     configs/body_2d_keypoint/topdown_heatmap/coco/td-hm_ViTPose-base_8xb64-210e_coco-256x192.py \
#     work_dirs/td-hm_ViTPose-base_3xb128-210e-f2_gm-256x192/td-hm_ViTPose-base_8xb64-210e_coco-256x192-216eae50_20230314.pth \
#     --save-predictions --output-root "pred/17" --draw-bbox --batch-size 128 --device cuda:0 \
#     --input "data/file_list_1.txt"

python demo/topdown_demo_batch.py \
    demo/mmdetection_cfg/rtmdet_m_640-8xb32_coco-person.py \
    https://download.openmmlab.com/mmpose/v1/projects/rtmpose/rtmdet_m_8xb32-100e_coco-obj365-person-235e8209.pth \
    configs/body_2d_keypoint/topdown_heatmap/coco/td-hm_ViTPose-base_8xb64-210e_coco-256x192.py \
    work_dirs/td-hm_ViTPose-base_3xb128-210e-f2_gm-256x192/td-hm_ViTPose-base_8xb64-210e_coco-256x192-216eae50_20230314.pth \
    --save-predictions --output-root "pred/17" --draw-bbox --batch-size 128 --device cuda:1 \
    --input "data/file_list_2.txt"

# 29 keypoints
# python demo/topdown_demo_batch.py \
#     demo/mmdetection_cfg/rtmdet_m_640-8xb32_coco-person.py \
#     https://download.openmmlab.com/mmpose/v1/projects/rtmpose/rtmdet_m_8xb32-100e_coco-obj365-person-235e8209.pth \
#     work_dirs/td-hm_ViTPose-base_3xb128-210e-f2_gm-256x192/td-hm_ViTPose-base_3xb128-210e-f2_gm-256x192.py \
#     work_dirs/td-hm_ViTPose-base_3xb128-210e-f2_gm-256x192/best_@0.1_PCKh_epoch_50.pth.zip \
#     --save-predictions --output-root "pred/29" --draw-bbox --batch-size 128 --device cuda:0 \
#     --input "data/file_list_1.txt"

# python demo/topdown_demo_batch.py \
#     demo/mmdetection_cfg/rtmdet_m_640-8xb32_coco-person.py \
#     https://download.openmmlab.com/mmpose/v1/projects/rtmpose/rtmdet_m_8xb32-100e_coco-obj365-person-235e8209.pth \
#     work_dirs/td-hm_ViTPose-base_3xb128-210e-f2_gm-256x192/td-hm_ViTPose-base_3xb128-210e-f2_gm-256x192.py \
#     work_dirs/td-hm_ViTPose-base_3xb128-210e-f2_gm-256x192/best_@0.1_PCKh_epoch_50.pth.zip \
#     --save-predictions --output-root "pred/29" --draw-bbox --batch-size 128 --device cuda:1 \
#     --input "data/file_list_2.txt"